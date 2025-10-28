// Script básico: nav móvil, year y smooth scroll
document.addEventListener('DOMContentLoaded', function(){
	// Año en el footer
	const y = new Date().getFullYear();
	const elYear = document.getElementById('year');
	if(elYear) elYear.textContent = y;

	// Nav toggle
	const toggle = document.querySelector('.nav-toggle');
	const nav = document.getElementById('main-nav');
	if(toggle && nav){
		toggle.addEventListener('click', function(){
			const expanded = this.getAttribute('aria-expanded') === 'true';
			this.setAttribute('aria-expanded', String(!expanded));
			nav.classList.toggle('open');
		});
	}

	// Smooth scroll for internal links
	document.querySelectorAll('a[href^="#"]').forEach(a=>{
		a.addEventListener('click', function(e){
			const href = this.getAttribute('href');
			if(href && href.startsWith('#')){
				const target = document.querySelector(href);
				if(target){
					e.preventDefault();
					target.scrollIntoView({behavior:'smooth', block:'start'});
					// close nav on mobile
					if(nav && nav.classList.contains('open')){
						nav.classList.remove('open');
						if(toggle) toggle.setAttribute('aria-expanded','false');
					}
				}
			}
		});
	});
});

