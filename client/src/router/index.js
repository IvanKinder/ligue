import Vue from 'vue';
import Router from 'vue-router';
import Client from '@/components/Client';
import Playbooks from '@/components/Playbooks';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Client',
      component: Client,
    },
    {
      path: '/playbooks/',
      name: 'Playbooks',
      component: Playbooks,
    },
  ],
});
