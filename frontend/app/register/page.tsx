"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function RegisterPage() {
  const router = useRouter();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleRegister = async () => {
    setLoading(true);
    setError("");

    try {
      const res = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (!res.ok) {
        throw new Error("Registration failed");
      }

      router.push("/login");
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Something went wrong");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-zinc-950">
      <div className="w-full max-w-md rounded-2xl bg-zinc-900 p-8 shadow-xl">
        <h1 className="mb-6 text-center text-3xl font-bold text-white">
          Create account
        </h1>

        {error && (
          <div className="mb-4 rounded-md bg-red-500/10 p-3 text-sm text-red-400">
            {error}
          </div>
        )}

        <div className="space-y-4">
          <input
            className="w-full rounded-lg bg-zinc-800 p-3 text-white placeholder-zinc-400 outline-none ring-1 ring-zinc-700 focus:ring-2 focus:ring-blue-500"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="password"
            className="w-full rounded-lg bg-zinc-800 p-3 text-white placeholder-zinc-400 outline-none ring-1 ring-zinc-700 focus:ring-2 focus:ring-blue-500"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            onClick={handleRegister}
            disabled={loading}
            className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-500 disabled:opacity-50"
          >
            {loading ? "Creating account..." : "Create account"}
          </button>
        </div>

        <p className="mt-6 text-center text-sm text-zinc-400">
          Already have an account?{" "}
          <a href="/login" className="text-blue-400 hover:underline">
            Sign in
          </a>
        </p>
      </div>
    </div>
  );
}
