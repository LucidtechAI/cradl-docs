// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Cradl documentation',
  tagline: 'No-code AI data-extraction for any document',
  url: 'https://docs.cradl.ai',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'throw',
  favicon: 'img/favicon.png',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'LucidtechAI', // Usually your GitHub org/user name.
  projectName: 'cradl-docs', // Usually your repo name.


  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          breadcrumbs: true,
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
    [
      'redocusaurus',
      {
        // debug: Boolean(process.env.DEBUG || process.env.CI),
        specs: [
          {
            spec: './static/oas.yaml',
            route: '/rest-api-reference/',
          }
        ],
        theme: {
          primaryColor: '#5f59f7',
          redocOptions: { hideDownloadButton: false },
        },
      },
    ],
  ],

  scripts: [
    '/rudderAnalytics.js'
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/cradl-social-card.png',

      navbar: {
        logo: {
          alt: 'Cradl AI logo',
          src: 'img/logo/docs-logo-black.svg',
          srcDark: 'img/logo/cradl-docs-white.svg',
          href: '/',
          target: '_self',
        
        },
            // hideOnScroll: true,
        items: [
        //   {
        //   to: '/blog', 
        //   label: 'Changelog', 
        //   position: 'right'
        //   },
          {
            href: 'https://app.cradl.ai/flows',
            label: 'Open Cradl AI',
            position: 'right',
            className: 'button button--primary button--md navbar-btn utils-mr-8'
          },
         ],
      },
      docs: {
        // sidebar: {
        //   hideable: true,
        // },
      },
    
      footer: {
        logo: {
          alt: 'Cradl AI logo',
          src: 'img/logo/cradl-docs-black.svg',
          srcDark: 'img/logo/cradl-docs-white.svg',
          href: '/',
        },
        links: [
          {
            title: 'Cradl AI',
            items: [
              {
                label: 'Cradl AI site',
                href: 'https://cradl.ai',
              },
              {
                label: 'Cradl AI app',
                href: 'https://app.cradl.ai',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/CradlAI',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/Cradl_AI',
              },
            ],
          },
          {
            title: 'GitHub',
            items: [
              {
                label: 'CLI',
                href: 'https://github.com/lucidtechAI/las-cli',
              },
              {
                label: 'Python SDK',
                href: 'https://github.com/lucidtechAI/las-sdk-python',
              },
              {
                label: 'JavaScript SDK',
                href: 'https://github.com/lucidtechAI/las-sdk-js',
              },
              {
                label: '.NET SDK',
                href: 'https://github.com/lucidtechAI/las-sdk-net',
              },
              {
                label: 'Java SDK',
                href: 'https://github.com/lucidtechAI/las-sdk-java',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Lucidtech AS. All rights reserved.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),

    plugins: [
      async function myPlugin(context, options) {
        return {
          name: "docusaurus-tailwindcss",
          configurePostCss(postcssOptions) {
            // Appends TailwindCSS and AutoPrefixer.
            postcssOptions.plugins.push(require("tailwindcss"));
            postcssOptions.plugins.push(require("autoprefixer"));
            return postcssOptions;
          },
        };
      },
    ],
};

export default config;
