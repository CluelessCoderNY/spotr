const puppeteer = require("puppeteer");
const getUrls = require("./urls");

const postUrl = "https://newyork.craigslist.org/search/rva?postedToday=1";

const main = async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  const urls = await getUrls(postUrl);

  const resolvedData = [];

  for (let i = 0; i < 2; i++) {
    await page.goto(urls[i], { waitUntil: "networkidle2" });

    return await page.evaluate(() => {
      const title = document.querySelector('span[id="titletextonly"]')
        .innerText;
      const price = document.querySelector('span[class="price"]').innerText;
      const description = document.querySelector('section[id="postingbody"]')
        .innerText;
      const postAge = document.querySelector('time[class="date timeago"]')
        .innerText;

      const rawTags = document.querySelectorAll('p[class="attrgroup"] span');
      const convertedTags = Array.prototype.slice.call(rawTags);
      const tags = convertedTags.map(tag => tag.innerText);

      const nodes = document.querySelector('div[id="thumbs"]').childNodes;
      const convertedNodes = Array.prototype.slice.call(nodes);
      const images = convertedNodes.map(node => node.getAttribute("href"));

      const mapLat = document
        .querySelector('div[id="map')
        .getAttribute("data-latitude");
      const mapLong = document
        .querySelector('div[id="map')
        .getAttribute("data-longitude");

      resolvedData.push({
        title,
        price,
        description,
        postAge,
        tags,
        images,
        mapLat,
        mapLong
      });
    });
  }

  console.log(resolvedData);
};

main();
