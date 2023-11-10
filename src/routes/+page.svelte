<main>
  <h1>GeoHuemul</h1>
  <div class="flex-row">
    <div class="link">
      <a class="preview" href="maps">
        <img src="/maps_prev2.png" alt="maps preview" />
      </a>
      <p>Maps</p>
    </div>
    <div class="link">
      <a class="preview" href="play">
        <img src="/maps_prev2.png" alt="maps preview" />
      </a>
      <p>Play</p>
    </div>
    <div class="link">
      <a class="preview" href="create">
        <img src="/maps_prev2.png" alt="maps preview" />
      </a>
      <p>Create</p>
    </div>
  </div>
</main>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Libre+Franklin&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Kanit&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

  main {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  h1 {
    font-family: 'Poppins', 'Kanit', 'Libre Franklin', sans-serif;
    font-size: 5rem;
    font-weight: 600;
  }

  .flex-row {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    margin-bottom: 10rem;
  }

  .preview {
    width: 12rem;
    height: 12rem;
    border-radius: 100%;
    border: 1px solid black;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    & :hover {
      opacity: 0.5;
    }
  }

  .link {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  img {
    height: 12rem;;
    transition: all 0.15s ease-in-out;
  }

  img:hover {
    height: 14rem;
  }
</style>