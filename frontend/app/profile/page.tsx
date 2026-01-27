"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function ProfilePage() {
  const router = useRouter();

  const username =
    typeof window !== "undefined"
      ? localStorage.getItem("username")
      : null;

  useEffect(() => {
    if (!username) {
      router.push("/login");
    }
  }, [username, router]);

  if (!username) {
    return null; // prevents UI flash before redirect
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-zinc-950">
      <div className="rounded-2xl bg-zinc-900 p-8 text-white shadow-xl">
        <h1 className="text-2xl font-bold mb-4">Profile</h1>
        <p className="text-zinc-300">Welcome, {username}</p>
      </div>
    </div>
  );
}
