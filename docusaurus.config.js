// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Cradl documentation',
  tagline: 'Dinosaurs are cool',
  url: 'https://docs.cradl.ai',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.png',
  organizationName: 'lucidtechAI', // Usually your GitHub org/user name.
  projectName: 'cradl-docs', // Usually your repo name.
  plugins: ['docusaurus-plugin-sass', require.resolve('docusaurus-lunr-search')],
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
          editUrl: 'https://github.com/lucidtechAI/cradl-docs/edit/master/docs/',
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/lucidtechAI/cradl-docs/edit/master/blog/',
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
            specUrl: './docs/reference/restapi/oas.yaml',
            routePath: '/rest-api-reference/',
          }
        ],
        theme: {
          primaryColor: '#1890ff',
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
        defaultMode: 'dark'
      },
      navbar: {
        logo: {
          alt: 'Cradl AI logo',
          src: 'img/logo-light_mode.svg',
          srcDark: 'img/logo-dark_mode.svg',
          href: 'https://docs.cradl.ai/',
          target: '_self',
        },
        items: [
          {
            type: 'doc',
            docId: 'index',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/lucidtechAI',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Docs',
                to: '/',
              },
            ],
          },
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
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/CradlAI',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/Cradl_AI',
              },
              {
                label: 'Cradl AI site',
                href: 'https://cradl.ai',
              },
              {
                label: 'Cradl AI app',
                href: 'https://app.cradl.ai',
              },
            ]
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
              {
                label: 'GitHub',
                href: 'https://github.com/lucidtechAI',
              },
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
