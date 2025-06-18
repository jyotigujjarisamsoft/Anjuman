# anjuman/api.py


import frappe
from frappe import _

@frappe.whitelist()
def create_tracker_from_relocation(application_id=None):
    if not application_id:
        frappe.throw("Application ID is required")

    # Fetch the Relocation Form using the application ID
    relocation_form = frappe.get_doc("Relocation Information Form", application_id)

    tracker = frappe.new_doc("Tracker")
    tracker.application_id = application_id

    # Set default status based on checkboxes
    if relocation_form.legal_assistance__guidance:
        tracker.legal_assistance_status = "Not Started"
    
    if relocation_form.job_search__placement_guidance:
        tracker.placement_guidance_status = "Not Started"

    if relocation_form.business_setup_guidance:
        tracker.business_setup_status = "Not Started"

    if relocation_form.investor_connection:
        tracker.investor_connection_status = "Not Started"

    if relocation_form.accommodation_assistance:
        tracker.accommodation_assistance_status = "Not Started"

    # Insert tracker
    tracker.insert(ignore_permissions=True)
    return tracker.name

@frappe.whitelist()
def fetch_rafiq_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'rafiq_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history

@frappe.whitelist()
def fetch_legal_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'legal_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history

@frappe.whitelist()
def fetch_placement_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'placement_guidance_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history


@frappe.whitelist()
def fetch_business_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'business_setup_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history


@frappe.whitelist()
def fetch_investor_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'investor_connection_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history


@frappe.whitelist()
def fetch_accommodation_remarks_history(docname):
    history = frappe.db.sql("""
        SELECT
            JSON_UNQUOTE(JSON_EXTRACT(changes.value, '$[2]')) AS new_value,
            v.owner AS changed_by,
            v.modified AS changed_on
        FROM `tabVersion` v,
        JSON_TABLE(
            JSON_EXTRACT(v.data, '$.changed'),
            '$[*]' COLUMNS (
                field_name VARCHAR(255) PATH '$[0]',
                value JSON PATH '$'
            )
        ) AS changes
        WHERE v.ref_doctype = 'Tracker'
        AND v.docname = %s
        AND changes.field_name = 'accommodation_assistance_remarks'
        ORDER BY v.modified
    """, (docname,), as_dict=True)

    remarks_history = ""
    for row in history:
        if row.new_value:
            remarks_history += f"Comment: {row.new_value}\n"
            remarks_history += f"Added by {row.changed_by} on {row.changed_on.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return remarks_history
