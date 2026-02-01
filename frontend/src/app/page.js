"use client";

import { useState } from "react";
import { login, register } from "@/lib/api";

export default function Home() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLogin, setIsLogin] = useState(true);
  const [msg, setMsg] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setMsg("");

    const res = isLogin
      ? await login(username, password)
      : await register(username, password);

    if (res.message) setMsg(res.message);
    if (isLogin && res.message === "Login successful") {
      window.location.href = "/dashboard";
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="bg-gray-800 p-8 rounded-xl w-96 shadow-lg">
        <h1 className="text-white text-3xl font-bold text-center mb-6">
          {isLogin ? "Login" : "Create Account"}
        </h1>

        {msg && <p className="text-center text-green-400 mb-4">{msg}</p>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            className="w-full p-3 rounded bg-gray-700 text-white"
            placeholder="Username"
            value={username}
            onChange={e => setUsername(e.target.value)}
            required
          />
          <input
            className="w-full p-3 rounded bg-gray-700 text-white"
            placeholder="Password"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />

          <button className="w-full bg-blue-600 hover:bg-blue-700 p-3 rounded text-white font-semibold">
            {isLogin ? "Login" : "Create Account"}
          </button>
        </form>

        <button
          className="mt-4 text-blue-400 w-full"
          onClick={() => setIsLogin(!isLogin)}
        >
          {isLogin ? "Create new account" : "Back to login"}
        </button>
      </div>
    </main>
  );
}
