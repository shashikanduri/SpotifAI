import React from 'react'
import { BsBoxArrowUpRight } from "react-icons/bs";

function Playlist({playlist}) {
  
  return (
    <>
      {playlist && 
        <div className = 'w-full flex justify-between p-6 items-center'>
          <div className = 'flex items-center justify-between gap-4'>
              <img src = { playlist.images[0]?.url ?? "" } width = "60" height = "60" />
              <p>{playlist.name}</p>
          </div>
          <a 
            className = 'hover:text-secondary flex items-center gap-2' 
            href = {playlist.external_urls.spotify} 
            target='_blank_'
          >
            Open on Spotify <BsBoxArrowUpRight />
          </a>
        </div>
      }
    </>
  )
}

export default Playlist;