import type { Route } from "./+types/home";
import { Welcome } from "../home/welcome";
import data from "../home/data/photos.json";
import type { Photos } from "../modules/schemas/data";
import { PhotosSchema } from "../modules/schemas/data";
import { PhotoGallery } from "../home/slideshow";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Chris Fleisch | Home" },
    {
      name: "description",
      content: "Welcome to Chris Fleisch's new React Router app!",
    },
  ];
}

export async function clientLoader({ params }: Route.ClientLoaderArgs) {
  const parsed = PhotosSchema.safeParse(data);
  if (!parsed.success) {
    console.error("Failed to parse photos.json:", parsed.error);
  }
  const photos: Photos = parsed.success ? parsed.data : [];
  return { photos };
}

// HydrateFallback is rendered while the client loader is running
export function HydrateFallback() {
  return <div>Loading...</div>;
}

export default function Home({ loaderData }: Route.ComponentProps) {
  const { photos } = loaderData;
  return (
    <>
      <Welcome />
      <PhotoGallery photos={photos} />
    </>
  );
}
