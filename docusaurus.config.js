// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Cradl documentation',
  tagline: 'AI-powered data capture APIs for any document',
  url: 'https://docs.cradl.ai',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'throw',
  favicon: 'img/favicon.png',
  organizationName: 'LucidtechAI', // Usually your GitHub org/user name.
  projectName: 'cradl-docs', // Usually your repo name.
  plugins: ['docusaurus-plugin-sass', require.resolve('docusaurus-lunr-search')],
  scripts: [
    {
      src: 'https://plausible.io/js/plausible.js',
      defer: true,
      "data-domain": process.env.PLAUSIBLE_DOMAIN,
    },
  ],
  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
          sidebarCollapsed: false,
          sidebarCollapsible: false,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
    [
      'redocusaurus',
      {
        debug: Boolean(process.env.DEBUG || process.env.CI),
        specs: [
          {
            specUrl: './oas.yaml',
            routePath: '/rest-api-reference/',
          }
        ],
        theme: {
          primaryColor: '#5f59f7',
          redocOptions: { hideDownloadButton: false },
        },
      },
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        respectPrefersColorScheme: true,
        defaultMode: 'light'
      },
      navbar: {
        title: 'Docs',
        logo: {
          alt: 'Cradl AI logo',
          src: 'img/cradl-docs-black.svg',
          srcDark: 'img/cradl-docs-white.svg',
          href: '/',
          target: '_self',
        }
      },
      footer: {
        logo: {
          alt: 'Cradl AI logo',
          src: 'img/cradl-docs-black.svg',
          srcDark: 'img/cradl-docs-white.svg',
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
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
