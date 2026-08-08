/* mind-upload.com — scenario page behavior (shared by EN and JA) */
document.documentElement.classList.add('js');
const progress = document.getElementById('progress');
const onScroll = () => {
  const h = document.documentElement;
  const max = h.scrollHeight - h.clientHeight;
  progress.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + '%';
};
document.addEventListener('scroll', onScroll, { passive: true });
onScroll();

const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// nav scrollspy
const navLinks = [...document.querySelectorAll('.primary-nav a')];
const map = new Map(navLinks.map(a => [a.getAttribute('href').slice(1), a]));
const spy = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      navLinks.forEach(a => a.classList.remove('active'));
      const link = map.get(e.target.id);
      if (link) link.classList.add('active');
    }
  });
}, { rootMargin: '-45% 0px -50% 0px' });
['abstract','scale','basis','scenario','fork','open','refs'].forEach(id => {
  const s = document.getElementById(id); if (s) spy.observe(s);
});

// era rail scrollytelling
const eras = [...document.querySelectorAll('.era')];
const railYear = document.getElementById('rail-year');
const railEra = document.getElementById('rail-era');
const railMetric = document.getElementById('rail-metric');
const railMetricLabel = document.getElementById('rail-metric-label');
const railFill = document.getElementById('rail-fill');
const nodes = [...document.querySelectorAll('.rail-node')];
const eraColors = ['#5fd6a4','#74c8b6','#7aa2ff','#9a9bf0','#bf9bef','#e08ad0'];
function setActive(i){
  const era = eras[i]; if(!era) return;
  railYear.textContent = era.dataset.year;
  railYear.style.color = eraColors[i];
  railEra.textContent = era.dataset.era;
  railEra.style.color = eraColors[i];
  railMetric.textContent = era.dataset.metric;
  railMetricLabel.textContent = era.dataset.metricLabel;
  nodes.forEach((n,k)=>{ n.classList.toggle('active',k===i); n.classList.toggle('done',k<i); });
  railFill.style.height = (((i+0.5)/eras.length)*100) + '%';
}
const eraSpy = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ setActive(eras.indexOf(e.target)); } });
}, { rootMargin:'-45% 0px -45% 0px', threshold:0 });
eras.forEach(e=>eraSpy.observe(e));
nodes.forEach((n,i)=>n.addEventListener('click',()=>{ setActive(i); eras[i].scrollIntoView({behavior:'smooth',block:'start'}); }));
// initialise rail to first phase
setActive(0);

// fork tabs
const ftabs = [...document.querySelectorAll('.ftab')];
const fpanels = [...document.querySelectorAll('.fork-panel')];
ftabs.forEach(t=>t.addEventListener('click',()=>{
  ftabs.forEach(x=>x.classList.remove('active'));
  t.classList.add('active');
  fpanels.forEach(p=>p.hidden = (p.dataset.route !== t.dataset.route));
}));

// mobile nav
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.primary-nav');
toggle.addEventListener('click', () => {
  const open = nav.classList.toggle('open');
  toggle.setAttribute('aria-expanded', open);
});
nav.addEventListener('click', e => { if (e.target.tagName === 'A') nav.classList.remove('open'); });
