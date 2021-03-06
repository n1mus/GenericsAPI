# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_GenericsReport(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='dev',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def build_heatmap_html(self, params, context=None):
        """
        :param params: instance of type "build_heatmap_html_params" (required
           params: tsv_file_path: matrix data in tsv format optional params:
           cluster_data: True if data should be clustered. Default: True
           dist_metric: distance metric used for clustering. Default:
           euclidean
           (https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial
           .distance.pdist.html) linkage_method: linkage method used for
           clustering. Default: ward
           (https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster
           .hierarchy.linkage.html)) -> structure: parameter "tsv_file_path"
           of String, parameter "cluster_data" of type "boolean" (A boolean -
           0 for false, 1 for true.), parameter "dist_metric" of String,
           parameter "linkage_method" of String
        :returns: instance of type "build_heatmap_html_result" -> structure:
           parameter "html_dir" of String
        """
        return self._client.run_job('kb_GenericsReport.build_heatmap_html',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('kb_GenericsReport.status',
                                    [], self._service_ver, context)
