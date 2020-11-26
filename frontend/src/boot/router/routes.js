/* eslint-disable comma-dangle */
/* eslint-disable object-property-newline */

const routes = [
  { path: '/auth/login', name: 'login', component: () => import('@view/auth/Login.vue') },
  {
    path: '', component: () => import('@view/layouts/Layout.vue'),
    children: [
      { path: '/', name: 'dashboard', component: () => import('@view/dashboard/Dashboard.vue') },
      { path: '/profiling/list', name: 'profilingList', component: () => import('@view/profiling/ProfilingList.vue') },
      { path: '/profiling/add', name: 'profilingAdd', component: () => import('@view/profiling/ProfilingAdd.vue') },
      { path: '/profilingFile/view/:Id', name: 'profilingFileView', component: () => import('@view/profiling/profilingFileView.vue') },
      // { path: '/profilingfile/view/:Id', name: 'profilingFileView', component: () => import('@view/dashboard/Dashboard.vue') },
    ]
  },
  { path: '*', redirect: '/404' },
  { path: '/404', name: '404', component: () => import('@view/errors/404.vue') }
]

export default routes
