<script>
	import Counter from './Counter.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcome_fallback from '$lib/images/svelte-welcome.png';
	import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from 'flowbite-svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<Table striped={true}>
		<TableHead>
		  <TableHeadCell>Currency</TableHeadCell>
		  <TableHeadCell>Name</TableHeadCell>
		  <TableHeadCell>Sell</TableHeadCell>
		  <TableHeadCell>Buy</TableHeadCell>
		  <TableHeadCell>
			<span class="sr-only"> Edit </span>
		  </TableHeadCell>
		</TableHead>
		<TableBody class="divide-y">
		  <TableBodyRow>
			<TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
			<TableBodyCell>Sliver</TableBodyCell>
			<TableBodyCell>Laptop</TableBodyCell>
			<TableBodyCell>$2999</TableBodyCell>
			<TableBodyCell>
			  <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500">
				Edit
			  </a>
			</TableBodyCell>
		  </TableBodyRow>
		  <TableBodyRow>
			<TableBodyCell>Microsoft Surface Pro</TableBodyCell>
			<TableBodyCell>White</TableBodyCell>
			<TableBodyCell>Laptop PC</TableBodyCell>
			<TableBodyCell>$1999</TableBodyCell>
			<TableBodyCell>
			  <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500">
				Edit
			  </a>
			</TableBodyCell>
		  </TableBodyRow>
		  <TableBodyRow>
			<TableBodyCell>Magic Mouse 2</TableBodyCell>
			<TableBodyCell>Black</TableBodyCell>
			<TableBodyCell>Accessories</TableBodyCell>
			<TableBodyCell>$99</TableBodyCell>
			<TableBodyCell>
			  <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500">
				Edit
			  </a>
			</TableBodyCell>
		  </TableBodyRow>
		  <TableBodyRow>
			<TableBodyCell>Google Pixel Phone</TableBodyCell>
			<TableBodyCell>Gray</TableBodyCell>
			<TableBodyCell>Phone</TableBodyCell>
			<TableBodyCell>$799</TableBodyCell>
			<TableBodyCell>
			  <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500">
				Edit
			  </a>
			</TableBodyCell>
		  </TableBodyRow>
		  <TableBodyRow>
			<TableBodyCell>Apple Watch 5</TableBodyCell>
			<TableBodyCell>Red</TableBodyCell>
			<TableBodyCell>Wearables</TableBodyCell>
			<TableBodyCell>$999</TableBodyCell>
			<TableBodyCell>
			  <a href="/tables" class="font-medium text-blue-600 hover:underline dark:text-blue-500">
				Edit
			  </a>
			</TableBodyCell>
		  </TableBodyRow>
		</TableBody>
	  </Table>
</section>

<!--<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcome_fallback} alt="Welcome" />
			</picture>
		</span>

		to your new<br />SvelteKit app
	</h1>

	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2>

	<Counter />
</section> -->

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
