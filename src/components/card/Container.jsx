import React from 'react'

export default (props) => (
  <div className="text-xl ml-2">
    <div className='text-[0.9em] font-bold'></div>
    <div className="row-wrap mx-auto">
      <div {...props} className="flex flex-wrap -mx-2"/>
    </div>
  </div>
)