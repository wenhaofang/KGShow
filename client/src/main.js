import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// ant design 会修改全局样式，因此要重新适配
import 'ant-design-vue/lib/table/style/css'

import {
  Table
} from 'ant-design-vue'

createApp(App)
  .use(router)
  .use(store)
  .use(Table)
  .mount('#app')
