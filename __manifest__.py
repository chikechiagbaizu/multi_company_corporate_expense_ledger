{
    'name': 'Multi-Company Corporate Expense Ledger',
    'summary': 'Consolidated Multi-Company Corporate Expense Ledger',
    'description': """
    Enterprise Multi-Tenant Expense Management
    ==========================================
    * Enforces row-level security isolation across distinct company holdings using global record rules.
    * Optimised query data processing via read_group() to aggregate heavy datasets directly in PostgreSQL.
    * Automated administrative analytical script routines utilizing with_company() environment isolation context switches.
    """,
    'author': 'Chike Chiagbaizu',
    'maintainer': 'Chike Chiagbaizu',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto-install': False,
    'depends': [
        'base'
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