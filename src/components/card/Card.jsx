export default ({header, title, description}) => (
      // <div className="flex flex-wrap -mx-2">
          <div className="column flex p-2 w-1/2  overflow-hidden">
              <div className="card w-full border overflow-hidden shadow rounded-xl">
                  <div className="relative bg-gray-700 h-32 w-full sm:h-auto" style={{paddingBottom: '50%' }}>
                      <img className="card__img top-0 h-full w-full object-cover absolute"  src="//source.unsplash.com/500x301/?nature" />
                  </div>
                  <div className="p-4">
                      <div className="text-xs tracking-wide uppercase">{header}</div>
                      <h3 className="text-sm my-1">{title}</h3>
                      <p className="text-sm">{description}</p>
                  </div>
              </div>
          </div>
        // </div>
)