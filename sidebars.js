/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  mySidebar: [
    {
      type: 'category',
      label: 'Overview',
      items: [
        {
          type: 'autogenerated',
          dirName: 'overview', // Generate sidebar slice from docs/preliminaries
        }
      ],
    },
    {
      type: 'category',
      label: 'Getting started',
      items: [
        {
          type: 'autogenerated',
          dirName: 'get-started', // Generate sidebar slice from docs/get-started
        }
      ],
    },
    {
      type: 'category',
      label: 'Human in the loop',
      items: [
        {
          type: 'autogenerated',
          dirName: 'human-in-the-loop', // Generate sidebar slice from docs/human-in-the-loop
        }
      ],
    },
    {
      type: 'category',
      label: 'Integrations',
      items: [
        {
          type: 'autogenerated',
          dirName: 'integrations', // Generate sidebar slice from docs/integrations
        }
      ],
    },
    {
      type: 'category',
      label: 'Concepts',
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: 'autogenerated',
          dirName: 'concepts', // Generate sidebar slice from docs/concepts
        }
      ],
    },
    {
      type: 'category',
      label: 'Reference',
      collapsible: true,
      collapsed: true,
      items: [
        'reference/authentication',
        'reference/cli',
        'reference/restapi',
        'reference/python',
        {
          type: 'autogenerated',
          dirName: 'reference/sdks', // Generate sidebar slice from docs/reference
        },
        'reference/quotas',
      ],
    },
    {
      type: 'category',
      label: 'Legal',
      collapsible: true,
      collapsed: true,
      items: [
        {
          type: 'autogenerated',
          dirName: 'legal', // Generate sidebar slice from docs/legal
        }
      ],
    },
    'questions'
  ]
};

module.exports = sidebars;
