"""Refreshes Material Views."""
import datetime
import time

from django.db import connection

from onebarangay_psql.statistics.models import RefreshMaterializedView


def refresh_mv():
    """Refresh Materialized Views in the Database."""
    start_time = time.monotonic()
    with connection.cursor() as cursor:
        cursor.execute(
            """
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_total;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_signup;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_signup_monthly;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_appointment;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_login;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_user_login_monthly;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_age_group;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_citizenship;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_civil_status;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_average;
        REFRESH MATERIALIZED VIEW CONCURRENTLY materialized_statistics_social_class;
        """
        )
    end_time = time.monotonic()

    RefreshMaterializedView.objects.create(
        duration=datetime.timedelta(seconds=end_time - start_time)
    )
