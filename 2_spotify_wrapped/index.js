window.onSpotifyWebPlaybackSDKReady = () => {
  const token = 'BQB1WJlvMCgoXqGLlV7HiebU-C7W8SZ5267fNhCMpM4s5rQiBfIXUePCoUm1Fr4FOik2Hxvz2GSZ9wPzyspcKuduNRtxYD7H35vlKMxrt67i9NkRL0tpDmqQBuDQ3DePH7M1O4qq9ADA_oLWpnjt_aLPA9pwqKhqffvqj8xnVwYAp6QvQmXJcPnnhphYAQd7HyB_kr0-W-Q95BYHaom-Jo3nLCkYea0g';
  const player = new Spotify.Player({
    name: 'Web Playback SDK Quick Start Player',
    getOAuthToken: cb => { cb(token); },
    volume: 0.5
  })

  // Ready
  player.addListener('ready', ({ device_id }) => {
    console.log('Ready with Device ID', device_id);
  });

  // Not Ready
  player.addListener('not_ready', ({ device_id }) => {
    console.log('Device ID has gone offline', device_id);
  });

  player.addListener('initialization_error', ({ message }) => {
      console.error(message);
  });

  player.addListener('authentication_error', ({ message }) => {
      console.error(message);
  });

  player.addListener('account_error', ({ message }) => {
      console.error(message);
  });
  
  player.connect();

  document.getElementById('togglePlay').onclick = function() {
    console.log("Toggling play!");
    player.togglePlay();
  };
};