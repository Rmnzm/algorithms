from leetcode.first_bad_version import Solution


class TestFirstBadVersion:
    func = Solution()

    def test_first_bad_version(self):
        result = self.func.first_bad_version(5)

        assert result == 1
