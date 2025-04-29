import { createRouter, createWebHistory  } from 'vue-router'
import MainPage from '../components/MainPage.vue';
import AnalysisPage from '../components/AnalysisPage.vue';

const routes = [
  { path: '/', name: 'MainPage', component: MainPage },
  { path: '/analysis', name: 'AnalysisPage', component: AnalysisPage },
];

const router = createRouter({
  history: createWebHistory (),
  routes
})

export default router



