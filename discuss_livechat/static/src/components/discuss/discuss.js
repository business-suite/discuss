/** @odoo-module **/

import { Discuss } from '@discuss/components/discuss/discuss';

import { patch } from 'web.utils';

const components = { Discuss };

patch(components.Discuss.prototype, 'discuss/static/src/components/discuss/discuss.js', {

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    mobileNavbarTabs(...args) {
        return [...this._super(...args), {
            icon: 'fa fa-comments',
            id: 'livechat',
            label: this.env._t("Livechat"),
        }];
    }

});
