import React from 'react'

function Playlist() {
  return (
    <div className = 'w-full flex justify-between p-8'>

        {/* playlist image and name */}
        <div className = 'w-[20%] flex'>
            <img></img>
            <p>Name</p>
        </div>

        <a>Open on Spotify</a>
    </div>
  )
}

export default Playlist;