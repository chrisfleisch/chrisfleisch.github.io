import { Welcome } from '../home/welcome'
import data from '../home/data/photos.json'
import type { Photos } from '../modules/schemas/data'
import { PhotosSchema } from '../modules/schemas/data'
import { PhotoGallery } from '../home/slideshow'

import type { Route } from './+types/home'

export function meta() {
  return [
    { title: 'Chris Fleisch | Home' },
    {
      name: 'description',
      content: "Welcome to Chris Fleisch's new React Router app!",
    },
  ]
}

export async function clientLoader() {
  const parsed = PhotosSchema.safeParse(data)
  if (!parsed.success) {
    console.error('Failed to parse photos.json:', parsed.error)
  }
  const photos: Photos = parsed.success ? parsed.data : []
  return { photos }
}

export default function Home({ loaderData }: Route.ComponentProps) {
  const { photos } = loaderData
  return (
    <>
      <Welcome />
      <PhotoGallery photos={photos} />
    </>
  )
}
