const API_URL = import.meta.env.VITE_API_URL;

export async function shortenUrl(url) {
  const response = await fetch(
    `${API_URL}/shorten`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({ url }),
    }
  );

  return response.json();
}

export async function getStats(shortCode) {

  const response = await fetch(
    `${API_URL}/stats/${shortCode}`
  );

  return response.json();
}