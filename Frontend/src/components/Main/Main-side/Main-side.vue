<template>
  <a-layout-sider
    class="main-side"
    v-model="collapsed"
    :trigger="null"
    collapsible
  >
    <!-- ANCHOR Trigger -->
    <a-layout-header>
      <div>
        <a-icon
          class="trigger"
          :type="collapsed ? 'right' : 'left'"
          @click="() => (collapsed = !collapsed)"
        />
      </div>
    </a-layout-header>
    <!-- ANCHOR menu -->
    <a-menu
      theme="dark"
      mode="inline"
      :open-keys="openKeys"
      @openChange="onOpenChange"
    >
      <a-menu-item key="1">
        <a-icon type="home" />
        <span>홈</span>
      </a-menu-item>

      <a-sub-menu
        v-for="{ menu_id, menu_name, menu_icon, sub_menus } in menuItems"
        class="main-side-submenu"
        :key="menu_id"
      >
        <span slot="title">
          <a-icon :type="menu_icon" />
          <span> {{ menu_name }}</span>
        </span>
        <a-menu-item v-for="sub_menu in sub_menus" :key="sub_menu.id">
          <div @click="openMenu" :data-id="sub_menu.link">
            {{ sub_menu.name }}
          </div>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </a-layout-sider>
</template>

<script>
import { LOAD_NAV_MENU } from "../../../config";

export default {
  name: "Main-side",

  components: {
    name: "Main-side",
  },

  data() {
    return {
      collapsed: false,
      menuItems: [],

      // NOTE for open current submenu only
      rootSubmenuKeys: ["sub1", "sub2", "sub3", "sub4", "sub5", "sub6", "sub7"],
      // NOTE for open the menu
      openKeys: ["sub1"],
    };
  },

  methods: {
    openMenu(e) {
      const { id } = e.target.dataset;
      this.$router.push(`/main/${id}`);
    },

    onOpenChange(openKeys) {
      const latestOpenKey = openKeys.find(
        (key) => this.openKeys.indexOf(key) === -1
      );
      if (this.rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
        this.openKeys = openKeys;
      } else {
        this.openKeys = latestOpenKey ? [latestOpenKey] : [];
      }
    },

    async loadNavMenus() {
      try {
        const response = await this.$http.get(LOAD_NAV_MENU);
        const validation = response && response.status === 200;
        !validation && new Error("cannot fetch the data");
        const { menuItems } = await response.data;
        this.menuItems = menuItems;
      } catch (error) {
        console.log("!!error fetch data!!");
      }
    },
  },
  // SECTION life Cycle
  mounted() {
    this.loadNavMenus();
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.main-side {
  background: $nav-side-color;

  > div {
    > header {
      background: $nav-side-color;
      padding: 0;
      height: 53px;

      > div {
        height: 100%;
        @include flexSet("flex-end", "center");

        > i {
          @include flexSet("center", "center");
          font-size: 12px;
          width: 23px;
          height: 23px;
          background: rgb(240, 242, 245);
          border-top-left-radius: 5px;
          border-bottom-left-radius: 5px;
        }
      }
    }

    > ul {
      background: $nav-side-color;
      color: #fff;
      width: 100%;
      border: 0;

      > li {
        border-bottom: 1px solid #444;
        margin: 0 !important;
        &:hover {
          background: $primary-color;
        }

        > ul {
          background: $nav-side-color;
        }
      }
    }
  }
}
</style>
