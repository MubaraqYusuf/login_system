"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    const res = await fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });

    if (!res.ok) return setError("Invalid credentials");

    const data = await res.json();
    localStorage.setItem("token", data.access_token);
    router.push("/profile");
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-black">
      <div className="bg-zinc-900 p-10 rounded-xl w-full max-w-md">
        <h1 className="text-3xl font-bold text-center mb-6">Welcome back</h1>

        {error && <p className="text-red-400 mb-4">{error}</p>}

        <input
          placeholder="Username"
          className="w-full mb-3 p-3 rounded bg-zinc-800"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          placeholder="Password"
          type="password"
          className="w-full mb-4 p-3 rounded bg-zinc-800"
          onChange={(e) => setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-blue-600 py-3 rounded hover:bg-blue-500"
        >
          Sign in
        </button>

        <p className="mt-4 text-sm text-center">
          Don’t have an account?{" "}
          <a href="/register" className="text-blue-400">
            Create one
          </a>
        </p>
      </div>
    </div>
  );
}
