import 'photoswipe/dist/photoswipe.css'

import { Gallery, Item } from 'react-photoswipe-gallery'

import type { Photos } from '../modules/schemas/data'

function Photo({
  title,
  datetaken,
  url_k,
  url_q,
  height_k,
  width_k,
}: {
  title: string
  datetaken: string
  url_k: string
  url_q: string
  height_k: number
  width_k: number
}) {
  return (
    <Item
      original={url_k}
      thumbnail={url_q}
      height={height_k}
      width={width_k}
      caption={title + ', ' + datetaken}
    >
      {({ ref, open }) => (
        <img
          ref={ref}
          onClick={open}
          src={url_q}
          alt={title + ', ' + datetaken}
        />
      )}
    </Item>
  )
}

export function PhotoGallery({ photos }: { photos: Photos }) {
  return (
    <article className="image_gallery">
      <Gallery withCaption>
        {photos.map((props, i) => (
          <Photo key={i} {...props} />
        ))}
      </Gallery>
    </article>
  )
}
