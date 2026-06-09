"use client";

import { Suspense, lazy, type HTMLAttributes } from "react";

const Spline = lazy(() => import("@splinetool/react-spline"));

interface HeroSplineBackgroundProps extends HTMLAttributes<HTMLDivElement> {
  scene?: string;
}

export default function HeroSplineBackground({
  scene = "https://prod.spline.design/us3ALejTXl6usHZ7/scene.splinecode",
  className = "",
  ...props
}: HeroSplineBackgroundProps) {
  return (
    <div
      className={`relative w-full h-full pointer-events-auto overflow-hidden ${className}`}
      {...props}
    >
      <Suspense fallback={null}>
        <Spline
          scene={scene}
          style={{ width: "100%", height: "100%", pointerEvents: "auto" }}
        />
      </Suspense>
      <div
        className="pointer-events-none absolute inset-0"
        style={{
          background: `
            linear-gradient(to right, rgba(0, 0, 0, 0.8), transparent 30%, transparent 70%, rgba(0, 0, 0, 0.8)),
            linear-gradient(to bottom, transparent 50%, rgba(0, 0, 0, 0.9))
          `,
        }}
      />
    </div>
  );
}
