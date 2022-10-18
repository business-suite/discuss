/** @odoo-module **/

import { DiscussWidget } from '@discuss/widgets/discuss/discuss';

import { action_registry } from 'web.core';
import { serviceRegistry } from 'web.core';

action_registry.add('discuss.widgets.discuss', DiscussWidget);
