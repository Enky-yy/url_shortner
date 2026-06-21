import { useState } from "react";
import { shortenUrl, getStats } from "./api";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const [loading, setLoading] = useState(false);

  const [stats, setStats] = useState(null);
  const [copied, setCopied] = useState(false);

  async function handleShorten() {
    if (!url) return;

    try {
      setLoading(true);

      const data = await shortenUrl(url);

      setShortUrl(data.shorten_url);

      const code = data.shorten_url.split("/").pop();

      const statsData = await getStats(code);

      setStats(statsData);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  async function copyLink() {
    await navigator.clipboard.writeText(shortUrl);

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  }

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-950 via-slate-900 to-black text-white flex items-center justify-center p-6">
      <div
        className="
w-full
max-w-2xl
backdrop-blur-xl
bg-white/5
border
border-white/10
shadow-2xl
rounded-3xl
p-8
"
      >
        <h1
          className="
text-5xl
font-black
text-center
mb-8
bg-linear-to-r
from-blue-400
to-purple-500
bg-clip-text
text-transparent
"
        >
          URL Shortener
        </h1>

        <div className="space-y-4">
          <input
            type="text"
            placeholder="Paste URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            className="
w-full
bg-linear-to-r
from-blue-600
to-indigo-600
p-3
rounded-xl
font-semibold
hover:scale-[1.02]
transition-all
duration-200
"
          />

          <button
            onClick={handleShorten}
            disabled={loading}
            className="w-full bg-blue-600 p-3 rounded-lg hover:bg-blue-700"
          >
            {loading ? "Loading..." : "Shorten URL"}
          </button>

          {shortUrl && (
            <div className="p-4 rounded-lg bg-slate-900 border border-slate-700">
              <p className="mb-2">Short URL</p>

              <a
                href={shortUrl}
                target="_blank"
                rel="noreferrer"
                className="text-blue-400 break-all"
              >
                {shortUrl}
              </a>

              <button
                onClick={copyLink}
                className="mt-4 w-full bg-green-600 p-2 rounded"
              >
                Copy Link
              </button>
            </div>
          )}

          {copied && (
            <p
              className="
      text-green-400
      text-center
      mt-2
    "
            >
              Copied to clipboard!
            </p>
          )}

          {stats && (
            <div
              className="
      mt-6
      grid
      grid-cols-3
      gap-4
    "
            >
              <div
                className="
        bg-slate-900
        border
        border-slate-700
        p-4
        rounded-xl
      "
              >
                <p className="text-slate-400 text-sm">Clicks</p>

                <h2 className="text-2xl font-bold">{stats.clicks}</h2>
              </div>

              <div
                className="
        bg-slate-900
        border
        border-slate-700
        p-4
        rounded-xl
      "
              >
                <p className="text-slate-400 text-sm">Code</p>

                <h2 className="font-bold">{stats.short_code}</h2>
              </div>

              <div
                className="
        bg-slate-900
        border
        border-slate-700
        p-4
        rounded-xl
      "
              >
                <p className="text-slate-400 text-sm">Status</p>

                <h2 className="font-bold text-green-400">Active</h2>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
