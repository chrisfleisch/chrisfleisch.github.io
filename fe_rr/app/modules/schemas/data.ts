import { z } from "zod";

export const PhotoSchema = z.object({
  title: z.string(),
  datetaken: z.string(),
  url_k: z.url(),
  url_q: z.url(),
  height_k: z.number().int().positive(),
  width_k: z.number().int().positive(),
});

export const PhotosSchema = z.array(PhotoSchema);

export type Photo = z.infer<typeof PhotoSchema>;
export type Photos = z.infer<typeof PhotosSchema>;
