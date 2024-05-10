import React, { useEffect } from 'react';
import HeaderText from './HeaderText';

export const CtaBox = () => {

  useEffect(() => {
    function playPause(video) {
      if (video.paused) {
        video.play();
      } else {
        video.pause();
      }
    }
    const videos = document.querySelectorAll('.video-container video');

    videos.forEach(video => {
      video.addEventListener('mouseenter', () => {
        video.controls = true;
      });

      video.addEventListener('mouseleave', () => {
        video.controls = false;
      });
    });
  }, []);

  return (
    <div className="bg-blue-50 dark:bg-transparent dark:border-gray-700 dark:border-solid dark:border-1 my-10 rounded-lg shadow-md">
      <h3 className='pb-4 lg:pb-8 pt-4 px-2 lg:px-4 font-semibold'>Get started quickly with data extraction and streamlining messy document flows.</h3>
      <div className='flex flex-col xl:flex-row min-h-[420px]'>
        <div className='basis-full xl:basis-1/2 p-4 lg:p-8 flex flex-col justify-between mb-4'>
          <HeaderText icon="/img/steps/01.svg" title="AI Studio" text="Tell your AI Model what to look for by training it on 15 of your own documents. After training, test how successfully it extracts data." />
          <div className="video-container">
            <video className='utils-shadow-md scale-95' poster="/video/ai_studio_thumb.png" width="100%">
              <source src="/video/ai_studio.mp4" type="video/mp4" />
            </video>
          </div>
        </div>
        <div className='basis-full xl:basis-1/2 p-4 lg:p-8 flex flex-col justify-between mb-4'>
          <HeaderText icon="/img/steps/02.svg" title="AI Validator" text="The AI Validator let's you stay in control. Automate eagerly or find the right balance between human inspection and AI automation." />
          <div className="video-container">
            <video className='utils-shadow-md scale-95 object-cover' width="100%" poster="/video/ai_validator_thumb.png">
              <source src="/video/ai_validator.mp4" type="video/mp4" />
            </video>
          </div>
        </div>
      </div>
      <div className='flex justify-center items-center pb-12'>
        <a href="/aiStudio/new-model" className='shadow-lg button button--primary button--md font-semibold text-lg h-min text-white' role="button">
          Get started
        </a>
      </div>
    </div>
  );
};

export default CtaBox;
