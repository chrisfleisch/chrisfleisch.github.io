import React from "react";
import "photoswipe/dist/photoswipe.css";

import { Gallery, Item } from "react-photoswipe-gallery";

function Photo({ title, datetaken, url_k, url_q, height_k, width_k }) {
  return (
    <Item
      original={url_k}
      thumbnail={url_q}
      height={height_k}
      width={width_k}
      caption={title + "<br><span>" + datetaken + "</span>"}
    >
      {({ ref, open }) => (
        <img
          ref={ref}
          onClick={open}
          src={url_q}
          alt={title + "<br><span>" + datetaken + "</span>"}
        />
      )}
    </Item>
  );
}

export default function MyGallery({ photos = [] }) {
  return (
    <article className="image_gallery">
      <header>
        <h1>Welcome</h1>
      </header>
      <Gallery withCaption>
        {photos.map((props, i) => (
          <Photo key={i} {...props} />
        ))}
      </Gallery>
    </article>
  );
}
