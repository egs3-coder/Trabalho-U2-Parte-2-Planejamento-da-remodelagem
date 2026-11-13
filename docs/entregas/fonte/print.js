// node print.js entrada.html saida.pdf a4|slides
const puppeteer = require('/opt/npm-tools/node_modules/puppeteer');
(async () => {
  const [inp, out, modo] = process.argv.slice(2);
  const b = await puppeteer.launch({ args: ['--no-sandbox', '--allow-file-access-from-files'] });
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(inp), { waitUntil: 'networkidle0' });
  if (modo === 'slides') {
    await p.pdf({ path: out, width: '1920px', height: '1080px', printBackground: true });
  } else {
    await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: '<div style="width:100%;font-family:Liberation Sans,Arial;font-size:7pt;text-align:right;padding-right:16mm;color:#222">Hemotrack · Rota Vital · Parte 2 — <span class="pageNumber"></span>/<span class="totalPages"></span></div>' });
  }
  await b.close();
})();
