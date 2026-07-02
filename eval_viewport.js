const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:5000/team.html');
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
  await page.screenshot({ path: 'mobile_before_click.png' });
  await page.evaluate(() => {
    document.querySelector('.hamburger').click();
  });
  await new Promise(r => setTimeout(r, 500)); // wait for animation
  await page.screenshot({ path: 'mobile_after_click.png' });
  const isNavVisibleAfterClick = await page.evaluate(() => {
    const el = document.querySelector('.nav-links');
    return window.getComputedStyle(el).display;
  });
  const navClasses = await page.evaluate(() => {
    return document.getElementById('navbar').className;
  });
  console.log('innerWidth:', innerWidth);
  console.log('outerWidth:', outerWidth);
  console.log('isNavVisible:', isNavVisible);
  console.log('isHamburgerVisible:', isHamburgerVisible);
  console.log('isNavVisibleAfterClick:', isNavVisibleAfterClick);
  console.log('navClasses:', navClasses);
  await browser.close();
})();
