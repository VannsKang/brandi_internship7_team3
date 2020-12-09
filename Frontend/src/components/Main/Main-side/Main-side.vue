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
import { mapState, mapActions } from "vuex";

export default {
  name: "Main-side",

  data() {
    return {
      collapsed: false,
      // NOTE for open current submenu only
      rootSubmenuKeys: ["sub1", "sub2", "sub3", "sub4", "sub5", "sub6", "sub7"],
      // NOTE for open the menu
      openKeys: ["sub1"],
    };
  },

  // SECTION life Cycle
  mounted() {
    this.updateMenuAction();
  },

  components: {},

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

    ...mapActions("navmenus", ["updateMenuAction"]),
  },

  computed: {
    ...mapState({
      menuItems: ({ navmenus }) => navmenus.menuItems,
    }),
  },
};
</script>

<style src="./Main-side.scss" lang="scss" scoped />
