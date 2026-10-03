"""
SYNAPSE HELIOS ID - Taxonomy & Database Integrity Unit Tests
"""
from app.data.taxonomy_db import AI_TAXONOMY_DATA
from app.data.languages_db import AI_LANGUAGES_DATA

def test_taxonomy_data_completeness():
    assert len(AI_TAXONOMY_DATA) == 6
    for cat in AI_TAXONOMY_DATA:
        assert cat.id
        assert cat.name
        assert cat.english_name
        assert len(cat.items) >= 1
        for item in cat.items:
            assert item.id
            assert item.title
            assert item.description
            assert len(item.key_mechanisms) >= 2
            assert len(item.pioneer_models) >= 2
            assert len(item.benchmarks) >= 2
            assert item.computational_complexity
            assert item.hardware_affinity
            assert item.risk_and_alignment

def test_languages_data_completeness():
    assert len(AI_LANGUAGES_DATA) == 7
    for lang in AI_LANGUAGES_DATA:
        assert lang.id
        assert lang.name
        assert lang.logo_url
        assert lang.role_indonesian
        assert lang.primary_ecosystem
        assert lang.performance_tier
        assert len(lang.specific_use_cases) >= 2
        assert lang.code_example
        assert len(lang.metrics) >= 3
