// Run using installed Node and playwright-core; no external network needed.
const {chromium} = require('/home/sgepner/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright-core');
const path = require('path');
const fs = require('fs');
(async()=>{
 const dir=path.join(__dirname,'results');
 const browser=await chromium.launch({executablePath:'/opt/google/chrome/chrome',headless:true,args:['--no-sandbox']});
 const page=await browser.newPage({viewport:{width:1200,height:1000},deviceScaleFactor:1});
 await page.route('http://**',r=>r.abort()); await page.route('https://**',r=>r.abort());
 await page.goto('file://'+path.join(dir,'lecture.html'),{waitUntil:'load'});
 await page.evaluate(()=>document.fonts.ready);
 const metrics=await page.evaluate(()=>{
   const headings=[...document.querySelectorAll('h2')].filter(e=>/^W6\.\d+/.test(e.textContent));
   return {width:document.documentElement.clientWidth,scrollWidth:document.documentElement.scrollWidth,
     images:[...document.images].map(e=>({loaded:e.complete&&e.naturalWidth>0,alt:e.alt,width:e.width,height:e.height})),
     sections:headings.map((h,i)=>({title:h.textContent,y:h.getBoundingClientRect().top+scrollY,
       bottom:i+1<headings.length?headings[i+1].getBoundingClientRect().top+scrollY:document.documentElement.scrollHeight}))};
 });
 if(metrics.scrollWidth>metrics.width)throw new Error('Horizontal document overflow');
 if(metrics.images.some(i=>!i.loaded))throw new Error('Broken image');
 fs.writeFileSync(path.join(dir,'render.json'),JSON.stringify(metrics,null,2));
 await page.setViewportSize({width:1200,height:Math.min(32760,Math.ceil(metrics.sections.at(-1).bottom))});
 for(let i=0;i<metrics.sections.length;i++){
   const s=metrics.sections[i];
   await page.screenshot({captureBeyondViewport:true,path:path.join(dir,`section_${String(i+1).padStart(2,'0')}.png`),clip:{x:0,y:Math.floor(s.y),width:1200,height:Math.ceil(s.bottom-s.y)}});
 }
 fs.writeFileSync(path.join(dir,'render.json'),JSON.stringify(metrics,null,2));
 await browser.close(); console.log(`Rendered ${metrics.sections.length} sections; ${metrics.images.length} images; no broken images or horizontal overflow`);
})().catch(e=>{console.error(e);process.exit(1)});
