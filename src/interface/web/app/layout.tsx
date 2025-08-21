import type { Metadata } from "next";
import { noto_sans, noto_sans_arabic } from "@/app/fonts";
import "./globals.css";
import "./globals-print.css";
import { ContentSecurityPolicy } from "./common/layoutHelper";
import { ThemeProvider } from "./components/providers/themeProvider";

export const metadata: Metadata = {
    title: "Aletheia - Ask Anything",
    description:
        "Aletheia is a personal knowledge assistant. It helps you understand better and create faster.",
    icons: {
        icon: "/favicon.ico",
        apple: "/Aletheia_logo.svg",
    },
    manifest: "/aletheia.webmanifest",
    keywords:
        "knowledge assistant, productivity, AI, Aletheia, open source, model agnostic, research, productivity tool, personal assistant, personal knowledge assistant, personal productivity assistant",
    openGraph: {
        siteName: "Aletheia",
        title: "Aletheia",
        description:
            "Aletheia is a personal knowledge assistant. It helps you understand better and create faster.",
        url: "https://kodan.space",
        type: "website",
        images: [
            {
                url: "/Aletheia_logo.svg",
                width: 256,
                height: 256,
            },
        ],
    },
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html
            lang="en"
            className={`${noto_sans.variable} ${noto_sans_arabic.variable}`}
            suppressHydrationWarning
        >
            <head>
                <script
                    dangerouslySetInnerHTML={{
                        __html: `
                            try {
                                if (localStorage.getItem('theme') === 'dark' ||
                                    (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                                    document.documentElement.classList.add('dark');
                                }
                            } catch (e) {}
                        `,
                    }}
                />
            </head>
            <ContentSecurityPolicy />
            <body>
                <ThemeProvider>{children}</ThemeProvider>
            </body>
        </html>
    );
}
