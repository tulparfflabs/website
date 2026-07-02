const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:5000/index.html');
  await page.screenshot({ path: 'local_screenshot.png' });
  await browser.close();
})();
