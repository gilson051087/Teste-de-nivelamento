import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import BuscaOperadoras from '../components/BuscaOperadoras.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/buscar', component: BuscaOperadoras },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;


