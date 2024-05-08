import React from 'react'
import BoxContainer from './BoxContainer'
import Box from './Box'
import HeaderText from './HeaderText'

export const CtaBox = () => (
  <div className="  bg-blue-50  dark:bg-transparent dark:border-gray-700 dark:border-solid dark:border-1 my-10 rounded-lg shadow-md">
    <h3 className='pb-4 lg:pb-8 pt-4 px-2 lg:px-4 font-semibold'>Get started quickly with data extraction and streamlining   messy document flows.</h3>
    <div className='flex flex-col xl:flex-row min-h-[420px]'>
      <div className='basis-full xl:basis-1/2 p-4 lg:p-8 flex flex-col justify-between mb-4'>
        <HeaderText icon="/img/steps/01.svg" title="AI Studio" text="Tell your AI Model what to look for by training it on 15 of your own documents. After training, test how successfullly it extracts data." />
        <video className='shadow-md scale-95' width="100%" controls>
            <source src="/video/ai_studio.mp4" type="video/mp4" />
        </video>
      </div>
      <div className='basis-full xl:basis-1/2 p-4 lg:p-8 flex flex-col justify-between mb-4'>
        <HeaderText icon="/img/steps/02.svg" title="AI Validator" text="The AI Validator let's you stay in control. Automate eagerly or find the right balance between human inspection and AI automation." />
        <video className='shadow-md scale-95' width="100%" controls>
            <source src="/video/ai_validator.mp4" type="video/mp4" />
        </video>
      </div>
    </div>
      
        <div className='flex justify-center items-center pb-12'>
          <a href="/aiStudio/new-model" className=' button button--primary button--md font-semibold text-lg h-min text-white' role="button">
            Get started 
          </a>
        </div>
    {/* </div>  */}
  </div>
);
export default CtaBox;