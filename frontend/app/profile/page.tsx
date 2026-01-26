"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type User = {
  id: number;
  username: string;
};

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const username =
    typeof window !== "undefined" ? localStorage.getItem("username") : null;

  useEffect(() => {
    if (!username) {
      router.push("/");
      return;
    }

    const fetchProfile = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:8000/profile/${username}`);

        if (!res.ok) {
          throw new Error("Profile not found");
        }

        const data: User = await res.json();
        setUser(data);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("Something went wrong");
        }
        router.push("/");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [username, router]);

  const handleLogout = () => {
    localStorage.removeItem("username");
    router.push("/");
  };

  const handleDelete = async () => {
    if (!username) return;

    try {
      const res = await fetch(`http://127.0.0.1:8000/delete/${username}`, {
        method: "DELETE",
      });

      if (!res.ok) {
        throw new Error("Could not delete account");
      }

      handleLogout();
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Something went wrong");
      }
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-zinc-950">
        <p className="text-white">Loading...</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-zinc-950">
      <div className="w-full max-w-md rounded-2xl bg-zinc-900 p-8 shadow-xl">
        <h1 className="mb-6 text-center text-3xl font-bold text-white">
          Profile
        </h1>

        {error && (
          <div className="mb-4 rounded-md bg-red-500/10 p-3 text-sm text-red-400">
            {error}
          </div>
        )}

        <div className="mb-4 text-center text-white">
          <p>
            <strong>Username:</strong> {user?.username}
          </p>
          <p>
            <strong>ID:</strong> {user?.id}
          </p>
        </div>

        <div className="flex gap-3">
          <button
            onClick={handleLogout}
            className="w-full rounded-lg bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-500"
          >
            Logout
          </button>

          <button
            onClick={handleDelete}
            className="w-full rounded-lg bg-red-600 py-3 font-semibold text-white transition hover:bg-red-500"
          >
            Delete Account
          </button>
        </div>
      </div>
    </div>
  );
}
