<script lang="ts">
 	import fs from 'fs';
	import path from 'path';
  import { page } from '$app/stores';  
	import SectionTitle from '$components/SectionTitle.svelte';

	// export function get(p) {
  // 	let output = [];
  //   const fullpath = path.join('./src/routes', p);
  //   console.log(fullpath);
  //   const entries = fs.readdirSync(fullpath);
  //   console.log(path.join(fullpath, entries[0]));
  //   const directories = entries.filter((entry: string) => fs.statSync(path.join(fullpath, entry)).isDirectory());
  //   console.log(directories);
  //   
  //   for (const dir of directories) {
  //     output.push({
  //       name: dir[0].toUpperCase() + dir.slice(1).replace(/_/g, ' '),
  //       path: path.join(p, dir),
  //       children: get(path.join(p, dir))
  //     })
  //   }
  // 	
  // 	return output
	// }

  function get(p: string) {
    const output = [];
    const fullpath = path.join('./src/routes', p);
    const entries = fs.readdirSync(fullpath);
    const directories = entries.filter((entry: string) => fs.statSync(path.join(fullpath, entry)).isDirectory());
    for (const dir of directories) {
      const routesPath = path.join(fullpath, dir, 'routes.json');
      const routesContent = fs.readFileSync(routesPath, 'utf8');
      const routes = JSON.parse(routesContent);
      console.log(routes);
       output.push({
         name: dir[0].toUpperCase() + dir.slice(1).replace(/_/g, ' '),
         path: path.join(p, dir),
         children: routes.map((route: any) => {
           return {
             name: route.fname,
             path: path.join(p, dir, route.name)
           }
         })
      })
      }
      console.log(output);
    return output
  }

	const directories = get($page.url.pathname);
	console.log(JSON.stringify(directories, null, 2));

</script>

<main>
  <div class="m-16">
    <SectionTitle title="Games"/>
  </div>
  <section>
    {#each directories as entry, i}
    <div class="box relative" style="animation-delay: {2+i/4}s;">
      <div class="gradient-border absolute" />
      <div class="country">
        <div class="country-title">
          <a href={entry.path}>{entry.name}</a>
        </div>
        <div class="h-[2px] w-full bg-white" />
        <ul>
        {#each entry.children as child}
          <li>
            <a href={child.path}>{child.name}</a>
          </li>
          {/each}
        </ul>
      </div>
    </div>
      {/each}
  </section>
</main>

<style>
  main {
    padding: 4rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: white;
    width: 100%;
    height: 100%;
  }
  section {
    display: flex;
    flex-wrap: wrap;
    align-self: center;
    gap: 2rem;
    justify-content: center;
    width: 75%;
  }
  .country-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0;
    width: 100%;
  }

  .box {
    width: 40%;
    padding: 2px;
    display: flex;
    justify-content: center;
    align-items: center;
    transform: scale(0);
    animation-duration: 0.25s;
    animation-name: scale-in;
    animation-fill-mode: forwards;
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border-radius: 1rem;
    overflow: hidden;
    background-color: black;
  }
  .country {
    padding: 2rem;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    border-radius: 1rem;
    background-color: black;
  }

  /* CHANGE THIS */
  /* ADD SHOW MORE BUTTON */
  ul {
    width: 100%;
    max-height: 12rem;
    overflow: scroll;
  }

  @keyframes scale-in {
    0% {
      transform: scale(0);
    }
    100% {
      transform: scale(1);
    }
  }

  .gradient-border {
    width: 100%;
    height: 100%;
    background-image: linear-gradient(120deg, var(--light-blue) 0%, var(--purple) 100%);
    z-index: -100;
  }
</style>