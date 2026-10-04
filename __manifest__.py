{
    'name': 'Multi-Company Corporate Expense Ledger',
    'summary': 'Consolidated Multi-Company Corporate Expense Ledger',
    'description': """
    Enterprise Multi-Company Expense Management

    ============================================
    
    * Enforces multi-company data isolation using access control lists
    and record rules.

    * Optimised expense data aggregation using Odoo's read_group()
    for efficient reporting across large datasets.

    * Supports controlled cross-company reporting using with_company()
    to execute operations within the appropriate company context.

    * Provides role-based access controls and expense lifecycle
    restrictions for secure financial data management.
    """,
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.1.0',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto-install': False,
    'depends': [
        'base',
        'account',
    ],
    'data': [
        'security/corporate_expense_groups.xml',
        'security/ir.model.access.csv',
        'security/corporate_expense_record_rule.xml',
        'views/view_corporate_expense_form.xml',
        'views/view_corporate_expense_list.xml',
        'views/corporate_expense_actions.xml',
        'views/corporate_expense_menus.xml',
    ]
}