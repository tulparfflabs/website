const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:5000/index.html');
  const innerWidth = await page.evaluate(() => window.innerWidth);
  const outerWidth = await page.evaluate(() => window.outerWidth);
  const isNavVisible = await page.evaluate(() => {
    const el = document.querySelector('.nav-links');
    return window.getComputedStyle(el).display;
  });
  const isHamburgerVisible = await page.evaluate(() => {
    const el = document.querySelector('.hamburger');
    return window.getComputedStyle(el).display;
  });
  console.log('innerWidth:', innerWidth);
  console.log('outerWidth:', outerWidth);
  console.log('isNavVisible:', isNavVisible);
  console.log('isHamburgerVisible:', isHamburgerVisible);
  await browser.close();
})();
