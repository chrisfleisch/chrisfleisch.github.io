import { test, expect } from '@playwright/test'

test('home page loads with no errors', async ({ page }) => {
  const errors: string[] = []
  const failedRequests: string[] = []

  page.on('pageerror', (err) => errors.push(err.message))
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(msg.text())
  })
  page.on('response', (res) => {
    if (res.status() >= 400) failedRequests.push(`${res.status()} ${res.url()}`)
  })

  const response = await page.goto('/')
  expect(response?.ok()).toBeTruthy()

  await expect(page).toHaveTitle(/Chris Fleisch/)
  await expect(page.getByRole('banner')).toBeVisible()
  await expect(page.getByRole('contentinfo')).toBeVisible()

  expect(errors).toEqual([])
  expect(failedRequests).toEqual([])
})
